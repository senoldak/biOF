from datetime import date, timedelta
from typing import Optional
from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete

from bioseeder.config import get_settings
from bioseeder.database import get_db
from bioseeder.models import Company, DrugCandidate, ClinicalTrial, CatalystEvent, BioAlphaScore
from bioseeder.engine.bio_alpha import calculate_bio_alpha

router = APIRouter()


@router.post("/seed")
async def seed_database(
    db: AsyncSession = Depends(get_db),
    x_admin_key: Optional[str] = Header(None, alias="X-Admin-Key"),
):
    """Seed the database with institutional biotech companies, drug pipelines, and catalysts."""
    settings = get_settings()
    # Authorization guard: Require DEBUG mode or valid ADMIN_API_KEY
    if not settings.DEBUG:
        if not settings.ADMIN_API_KEY or x_admin_key != settings.ADMIN_API_KEY:
            raise HTTPException(
                status_code=403,
                detail="Forbidden: Database seeding is restricted. Provide valid X-Admin-Key or enable DEBUG mode.",
            )

    # Clean existing data
    await db.execute(delete(BioAlphaScore))
    await db.execute(delete(CatalystEvent))
    await db.execute(delete(ClinicalTrial))
    await db.execute(delete(DrugCandidate))
    await db.execute(delete(Company))
    await db.commit()

    today = date.today()

    # Curated institutional dataset
    seed_companies = [
        {
            "ticker": "VRTX",
            "name": "Vertex Pharmaceuticals",
            "exchange": "NASDAQ",
            "market_cap": 118500.0,
            "enterprise_value": 108000.0,
            "cash_and_equivalents": 10500.0,
            "quarterly_burn_rate": 650.0,
            "cash_runway_months": 48.5,
            "float_shares": 256.0,
            "short_interest_pct": 1.8,
            "drugs": [
                {
                    "code_name": "VX-548",
                    "generic_name": "Suzetrigine",
                    "brand_name": "Journavo",
                    "indication": "Moderate-to-Severe Acute Pain",
                    "therapeutic_area": "Neurology / Pain",
                    "target_tam": 5500.0,
                    "highest_phase": "NDA/BLA",
                    "mechanism_of_action": "Selective NaV1.8 inhibitor",
                    "trials": [
                        {
                            "nct_id": "NCT04208555",
                            "title": "Phase 3 Study of VX-548 Following Abdominoplasty",
                            "phase": "Phase 3",
                            "status": "Completed",
                            "primary_completion_date": today - timedelta(days=120),
                            "enrollment": 1118,
                        }
                    ],
                    "catalysts": [
                        {
                            "catalyst_type": "PDUFA",
                            "target_date": today + timedelta(days=22),
                            "date_precision": "EXACT",
                            "status": "UPCOMING",
                            "outcome": "PENDING",
                            "details": "FDA PDUFA target action date for NDA review of Suzetrigine in acute pain under Priority Review.",
                            "designations": ["Priority Review", "Breakthrough Therapy"],
                        }
                    ],
                },
                {
                    "code_name": "VX-880",
                    "generic_name": "Stem cell-derived islet cells",
                    "indication": "Type 1 Diabetes with Severe Hypoglycemia",
                    "therapeutic_area": "Endocrinology / Cell Therapy",
                    "target_tam": 8000.0,
                    "highest_phase": "Phase 1/2",
                    "mechanism_of_action": "Allogeneic stem cell-derived islet cells",
                    "trials": [
                        {
                            "nct_id": "NCT04786262",
                            "title": "Safety and Efficacy of VX-880 in Type 1 Diabetes",
                            "phase": "Phase 1/2",
                            "status": "Active, not recruiting",
                            "primary_completion_date": today + timedelta(days=180),
                            "enrollment": 17,
                        }
                    ],
                    "catalysts": [
                        {
                            "catalyst_type": "Phase 2 Readout",
                            "target_date": today + timedelta(days=75),
                            "date_precision": "MONTH",
                            "status": "UPCOMING",
                            "outcome": "PENDING",
                            "details": "Full Cohort C data readout on endogenous insulin secretion and HbA1c normalization.",
                            "designations": ["Fast Track", "Orphan Drug"],
                        }
                    ],
                },
            ],
        },
        {
            "ticker": "CRSP",
            "name": "CRISPR Therapeutics",
            "exchange": "NASDAQ",
            "market_cap": 4600.0,
            "enterprise_value": 3100.0,
            "cash_and_equivalents": 1900.0,
            "quarterly_burn_rate": 180.0,
            "cash_runway_months": 31.6,
            "float_shares": 82.0,
            "short_interest_pct": 12.4,
            "drugs": [
                {
                    "code_name": "CTX112",
                    "generic_name": "Allogeneic CD19 CAR-T",
                    "indication": "B-cell Malignancies & Lupus Nephritis",
                    "therapeutic_area": "Oncology / Autoimmune",
                    "target_tam": 4200.0,
                    "highest_phase": "Phase 1/2",
                    "mechanism_of_action": "CRISPR-Cas9 gene-edited allogeneic CAR-T",
                    "trials": [
                        {
                            "nct_id": "NCT05643742",
                            "title": "A Study Evaluating CTX112 in Relapsed/Refractory B-Cell Malignancies",
                            "phase": "Phase 1/2",
                            "status": "Recruiting",
                            "primary_completion_date": today + timedelta(days=90),
                            "enrollment": 120,
                        }
                    ],
                    "catalysts": [
                        {
                            "catalyst_type": "Phase 1/2 Readout",
                            "target_date": today + timedelta(days=35),
                            "date_precision": "EXACT",
                            "status": "UPCOMING",
                            "outcome": "PENDING",
                            "details": "Clinical readout for CTX112 in Systemic Lupus Erythematosus (SLE) at upcoming medical congress.",
                            "designations": ["Fast Track"],
                        }
                    ],
                }
            ],
        },
        {
            "ticker": "VKTX",
            "name": "Viking Therapeutics",
            "exchange": "NASDAQ",
            "market_cap": 6200.0,
            "enterprise_value": 5300.0,
            "cash_and_equivalents": 930.0,
            "quarterly_burn_rate": 45.0,
            "cash_runway_months": 62.0,
            "float_shares": 105.0,
            "short_interest_pct": 16.8,
            "drugs": [
                {
                    "code_name": "VK2735",
                    "generic_name": "Dual GLP-1/GIP receptor agonist",
                    "indication": "Obesity & Metabolic Disorders",
                    "therapeutic_area": "Metabolic / Obesity",
                    "target_tam": 25000.0,
                    "highest_phase": "Phase 3",
                    "mechanism_of_action": "Dual agonist of GLP-1 and GIP receptors (oral and subcutaneous)",
                    "trials": [
                        {
                            "nct_id": "NCT06512345",
                            "title": "Phase 3 Trial of Subcutaneous VK2735 in Adults with Obesity",
                            "phase": "Phase 3",
                            "status": "Recruiting",
                            "primary_completion_date": today + timedelta(days=210),
                            "enrollment": 2500,
                        }
                    ],
                    "catalysts": [
                        {
                            "catalyst_type": "Phase 3 Readout",
                            "target_date": today + timedelta(days=14),
                            "date_precision": "EXACT",
                            "status": "UPCOMING",
                            "outcome": "PENDING",
                            "details": "Oral tablet Phase 2 extension data and Phase 3 trial initiation milestone update.",
                            "designations": ["Fast Track"],
                        }
                    ],
                }
            ],
        },
        {
            "ticker": "SRPT",
            "name": "Sarepta Therapeutics",
            "exchange": "NASDAQ",
            "market_cap": 11200.0,
            "enterprise_value": 11600.0,
            "cash_and_equivalents": 850.0,
            "quarterly_burn_rate": 190.0,
            "cash_runway_months": 13.4,
            "float_shares": 96.0,
            "short_interest_pct": 9.2,
            "drugs": [
                {
                    "code_name": "SRP-9001",
                    "generic_name": "Delandistrogene moxeparvovec",
                    "brand_name": "Elevidys",
                    "indication": "Duchenne Muscular Dystrophy (Non-Ambulatory)",
                    "therapeutic_area": "Rare Disease / Neurology",
                    "target_tam": 4000.0,
                    "highest_phase": "Approved",
                    "mechanism_of_action": "AAVrh74 micro-dystrophin gene therapy",
                    "trials": [
                        {
                            "nct_id": "NCT05096221",
                            "title": "A Study of Delandistrogene Moxeparvovec in Subjects With DMD (EMBARK)",
                            "phase": "Phase 3",
                            "status": "Completed",
                            "primary_completion_date": today - timedelta(days=60),
                            "enrollment": 125,
                        }
                    ],
                    "catalysts": [
                        {
                            "catalyst_type": "AdCom Meeting",
                            "target_date": today + timedelta(days=8),
                            "date_precision": "EXACT",
                            "status": "UPCOMING",
                            "outcome": "PENDING",
                            "details": "FDA Advisory Committee meeting to review efficacy data for label expansion into non-ambulatory DMD patients.",
                            "designations": ["Breakthrough Therapy", "Orphan Drug", "Priority Review"],
                        }
                    ],
                }
            ],
        },
        {
            "ticker": "IOVA",
            "name": "Iovance Biotherapeutics",
            "exchange": "NASDAQ",
            "market_cap": 2800.0,
            "enterprise_value": 2400.0,
            "cash_and_equivalents": 420.0,
            "quarterly_burn_rate": 115.0,
            "cash_runway_months": 10.9,
            "float_shares": 270.0,
            "short_interest_pct": 19.5,
            "drugs": [
                {
                    "code_name": "LN-145",
                    "generic_name": "Lifileucel",
                    "brand_name": "Amtagvi",
                    "indication": "Metastatic Non-Small Cell Lung Cancer",
                    "therapeutic_area": "Oncology",
                    "target_tam": 6500.0,
                    "highest_phase": "Phase 2",
                    "mechanism_of_action": "Autologous Tumor-Infiltrating Lymphocyte (TIL) cell therapy",
                    "trials": [
                        {
                            "nct_id": "NCT04614103",
                            "title": "A Study of Lifileucel (LN-145) in Combination With Pembrolizumab in NSCLC",
                            "phase": "Phase 2",
                            "status": "Active, not recruiting",
                            "primary_completion_date": today + timedelta(days=45),
                            "enrollment": 180,
                        }
                    ],
                    "catalysts": [
                        {
                            "catalyst_type": "Phase 2 Readout",
                            "target_date": today + timedelta(days=42),
                            "date_precision": "EXACT",
                            "status": "UPCOMING",
                            "outcome": "PENDING",
                            "details": "Preliminary overall response rate (ORR) and duration of response (DOR) in frontline NSCLC combo cohort.",
                            "designations": ["Fast Track", "Orphan Drug"],
                        }
                    ],
                }
            ],
        },
        {
            "ticker": "NANO",
            "name": "Nanovest Therapeutics",
            "exchange": "NASDAQ",
            "market_cap": 85.0,  # Micro cap
            "enterprise_value": 90.0,
            "cash_and_equivalents": 12.0,
            "quarterly_burn_rate": 8.0,
            "cash_runway_months": 4.5,  # DILUTION HAZARD (< 6 months)
            "float_shares": 18.0,
            "short_interest_pct": 24.1,
            "drugs": [
                {
                    "code_name": "NV-101",
                    "generic_name": "Nanoparticle Paclitaxel Conjugate",
                    "indication": "Refractory Glioblastoma",
                    "therapeutic_area": "Oncology / CNS",
                    "target_tam": 1200.0,
                    "highest_phase": "Phase 2",
                    "mechanism_of_action": "Blood-brain barrier permeable nanoparticle taxane",
                    "trials": [
                        {
                            "nct_id": "NCT05988112",
                            "title": "Phase 2 Study of NV-101 in Recurrent Glioblastoma Multiforme",
                            "phase": "Phase 2",
                            "status": "Active, not recruiting",
                            "primary_completion_date": today + timedelta(days=15),
                            "enrollment": 45,
                        }
                    ],
                    "catalysts": [
                        {
                            "catalyst_type": "Phase 2 Readout",
                            "target_date": today + timedelta(days=12),
                            "date_precision": "EXACT",
                            "status": "UPCOMING",
                            "outcome": "PENDING",
                            "details": "Topline overall survival readout in recurrent GBM. High dilution risk flagged due to 4.5 months cash runway.",
                            "designations": ["Orphan Drug"],
                        }
                    ],
                }
            ],
        },
    ]

    companies_count = 0
    catalysts_count = 0

    for c_data in seed_companies:
        drugs_data = c_data.pop("drugs")
        company = Company(**c_data)
        db.add(company)
        await db.flush()
        companies_count += 1

        for d_data in drugs_data:
            trials_data = d_data.pop("trials", [])
            catalysts_data = d_data.pop("catalysts", [])

            drug = DrugCandidate(company_id=company.id, **d_data)
            db.add(drug)
            await db.flush()

            trial_id = None
            for t_data in trials_data:
                trial = ClinicalTrial(drug_id=drug.id, **t_data)
                db.add(trial)
                await db.flush()
                trial_id = trial.id

            for cat_data in catalysts_data:
                designations = cat_data.pop("designations", [])
                catalyst = CatalystEvent(
                    company_id=company.id,
                    drug_id=drug.id,
                    trial_id=trial_id,
                    **cat_data,
                )
                db.add(catalyst)
                await db.flush()
                catalysts_count += 1

                # Calculate quantitative Bio-Alpha score
                days_to_event = (catalyst.target_date - today).days
                breakdown = calculate_bio_alpha(
                    days_to_event=days_to_event,
                    therapeutic_area=drug.therapeutic_area,
                    phase=drug.highest_phase,
                    target_tam=drug.target_tam or 1000.0,
                    market_cap=company.market_cap or 500.0,
                    cash_runway_months=company.cash_runway_months or 12.0,
                    designations=designations,
                    insider_score=65.0,
                )

                score = BioAlphaScore(
                    catalyst_id=catalyst.id,
                    composite_score=breakdown.composite_score,
                    proximity_score=breakdown.proximity_score,
                    pos_score=breakdown.pos_score,
                    asymmetry_score=breakdown.asymmetry_score,
                    dilution_hazard_score=breakdown.dilution_hazard_score,
                    smart_money_score=breakdown.smart_money_score,
                    dilution_flag=breakdown.dilution_flag,
                )
                db.add(score)

    await db.commit()
    return {
        "status": "success",
        "message": "Database seeded with institutional biopharma data.",
        "companies_seeded": companies_count,
        "catalysts_seeded": catalysts_count,
    }
