-- Create schema for weather data
CREATE SCHEMA IF NOT EXISTS weather;

-- Create table for current weather data
CREATE TABLE IF NOT EXISTS weather.measurements (
    id SERIAL PRIMARY KEY,
    city_id INTEGER NOT NULL,
    temperature DECIMAL(5,2),
    feels_like DECIMAL(5,2),
    humidity INTEGER,
    pressure INTEGER,
    wind_speed DECIMAL(5,2),
    wind_direction INTEGER,
    description VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_current_weather_city_id ON weather.current_weather(city_id);

-- Create table for cities
CREATE TABLE IF NOT EXISTS weather.cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);