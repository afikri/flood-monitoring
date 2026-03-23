# 🌊 Flood Level Monitoring API
**Full-Stack Demo for Eurac Research (RECEPTIC IoT Developer Role)**  
**Author:** Abdul Fikri | **Date:** March 2026  
**Contact:** afikri@cseas.kyoto-u.ac.jp | +81 70 8905 7097

*A complete IoT pipeline: ESP32-like sensor → Django REST API → PostgreSQL → Threshold Alerting → React + Leaflet Dashboard*

---

## 🎯 Relevance to RECEPTIC Project

| RECEPTIC Requirement | This Demo | My CV Experience |
|---------------------|-----------|------------------|
| **Django Backend** | Django 5.2 LTS + DRF ViewSets | **MAHS (2024–Present):** Arches database management |
| **PostgreSQL** | Production-ready schema with indexes | **Aceh Green (2012):** Designed PostgreSQL databases for Aceh Government |
| **REST API Design** | Versioned `/api/v1/` endpoints | **UNICEF (2021):** Interoperable mechanisms with government systems |
| **IoT Data Ingestion** | Python simulator mimicking ESP32 | **BNPB (2023):** MHEWS SRS analysis & sensor requirements |
| **Geospatial Visualization** | React + Leaflet map dashboard | **UNICEF (2021):** SDG Dashboard development |
| **System Security** | CORS, server-side validation | **Better Work (2018):** Database security & unauthorized access prevention |

---

## Architecture Overview
┌─────────────────────────────────────────────────────────────────────────────┐
│                        FLOOD LEVEL MONITORING SYSTEM                        │
│                     Full-Stack IoT Pipeline for RECEPTIC                    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐      HTTP POST       ┌─────────────────────────────────┐
│   IoT Simulator │ ──────────────────>  │         Django Backend          │
│   (ESP32 Mimic) │   /api/v1/readings/  │         (Django 5.2 LTS)        │
│   Python +      │   JSON Payload:      │                                 │
│   requests lib  │   {water_level,      │  ┌───────────────────────────┐  │
│                 │    battery_pct,      │  │    DRF ViewSets           │  │
│                 │    station_id}       │  │    - StationViewSet       │  │
│                 │                      │  │    - ReadingViewSet       │  │
│                 │                      │  └─────────────┬─────────────┘  │
│                 │                      │                │                │
│                 │                      │  ┌─────────────▼─────────────┐  │
│                 │                      │  │   Server-Side Validation  │  │
│                 │                      │  │   - Alert status calc     │  │
│                 │                      │  │   - Threshold comparison  │  │
│                 │                      │  │   - Data integrity check  │  │
│                 │                      │  └─────────────┬─────────────┘  │
└─────────────────┘                      └────────────────────────────────┘
                                                         │ ORM
                                                         ▼
                                          ┌─────────────────────────────────┐
                                          │         PostgreSQL 15           │
                                          │      (flood_monitoring_db)      │
                                          │                                 │
                                          │  ┌───────────────────────────┐  │
                                          │  │   api_sensorstation       │  │
                                          │  │   - id, station_id        │  │
                                          │  │   - name, latitude        │  │
                                          │  │   - longitude, threshold  │  │
                                          │  └───────────────────────────┘  │
                                          │                                 │
                                          │  ┌───────────────────────────┐  │
                                          │  │   api_waterlevelreading   │  │
                                          │  │   - id, water_level       │  │
                                          │  │   - battery_pct, status   │  │
                                          │  │   - timestamp, station    │  │
                                          │  └───────────────────────────┘  │
                                          └────────────────────────────────┘
                                                           │
                         ┌─────────────────────────────────┼─────────────────────────────────┐
                         │                                 │                                 │
                         ▼                                 ▼                                 ▼
            ┌─────────────────────┐            ┌─────────────────────┐            ┌─────────────────────┐
            │   Django Admin      │            │   REST API          │            │   IoT Simulator     │
            │   /admin/           │            │   /api/v1/          │            │   (Data Ingestion)  │
            │   - CRUD stations   │            │   - GET stations    │            │   - POST readings   │
            │   - View readings   │            │   - GET readings    │            │   - Auto-alert      │
            │   - Manage users    │            │   - CORS enabled    │            │   - 10s interval    │
            └─────────────────────┘            └──────────┬──────────┘            └─────────────────────┘
                                                          │ HTTP GET
                                                          ▼
                                          ┌─────────────────────────────────┐
                                          │         Frontend                │
                                          │    React 18 + TypeScript        │
                                          │                                 │
                                          │  ┌───────────────────────────┐  │
                                          │  │   Leaflet Map Component   │  │
                                          │  │   - Station markers       │  │
                                          │  │   - Popup info            │  │
                                          │  │   - Real-time updates     │  │
                                          │  └───────────────────────────┘  │
                                          │                                 │
                                          │  ┌───────────────────────────┐  │
                                          │  │   Axios HTTP Client       │  │
                                          │  │   - API integration       │  │
                                          │  │   - Error handling        │  │
                                          │  └───────────────────────────┘  │
                                          └─────────────────────────────────┘