-- Create enum type first
CREATE TYPE statistics_type AS ENUM ('expense', 'revenue');

CREATE TABLE statistics (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    type statistics_type NOT NULL,
    location VARCHAR(255) NOT NULL,
    amount FLOAT NOT NULL
);

CREATE TABLE providers (
    provider_id SERIAL PRIMARY KEY,
    provider_name VARCHAR(100),
    provider_type VARCHAR(100),
    address VARCHAR(100),
    city VARCHAR(100),
    state_region VARCHAR(100),
    country VARCHAR(100),
    longitude VARCHAR(20),
    latitude VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    onboarding_stage TEXT NOT NULL DEFAULT 'not_contacted' CHECK (
        onboarding_stage IN (
            'not_contacted',
            'contacted',
            'demo_scheduled',
            'demo_done',
            'trial_started',
            'trial_ended',
            'contract_signed'
        )
    ),
    first_login TIMESTAMP DEFAULT NULL,
    last_active TIMESTAMP DEFAULT NULL
);


CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),
    national_id_number VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    height NUMERIC(5,2) CHECK (height > 0),
    weight NUMERIC(5,2) CHECK (weight > 0),
    address TEXT,
    city VARCHAR(100),
    state_region VARCHAR(100),
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Screenings (
    screening_id SERIAL PRIMARY KEY,
    patient_id INT,
    provider_id INT,
    screening_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    screening_type VARCHAR(100),
    notes VARCHAR(100),
    fasting_glucose NUMERIC(5,2) CHECK(fasting_glucose > 0),
    hba1c NUMERIC(5,2) CHECK(hba1c > 0),
    blood_pressure NUMERIC(5,2) CHECK(blood_pressure > 0),
    has_diabetes BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE SET NULL,
    FOREIGN KEY (provider_id) REFERENCES Providers(provider_id) ON DELETE SET NULL
);

CREATE TABLE Contracts (
    contract_id SERIAL PRIMARY KEY,
    provider_id INT,
    contract_name VARCHAR(100),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    pricing_model VARCHAR(100),
    agreed_rate NUMERIC(10,2),
    currency VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (provider_id) REFERENCES Providers(provider_id) ON DELETE SET NULL
);

CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,
    contract_id INT,
    transaction_type VARCHAR(100),
    amount NUMERIC(10,2),
    currency VARCHAR(100),
    converted_to_usd NUMERIC(10,2),
    transaction_date TIMESTAMP,
    descriptive_notes VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (contract_id) REFERENCES Contracts(contract_id) ON DELETE SET NULL
);

-- Create function for updating updated_at columns
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for all tables with updated_at
DO $$ 
DECLARE 
    tbl text;
BEGIN
    FOR tbl IN 
        SELECT table_name FROM information_schema.columns 
        WHERE column_name = 'updated_at' 
        AND table_schema = 'public'
    LOOP
        EXECUTE format('CREATE TRIGGER update_%s_updated_at
            BEFORE UPDATE ON %I
            FOR EACH ROW EXECUTE FUNCTION update_updated_at_column()', 
            tbl, tbl);
    END LOOP;
END$$;