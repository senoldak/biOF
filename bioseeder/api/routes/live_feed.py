from datetime import datetime, timezone
from fastapi import APIRouter
from bioseeder.api.schemas import LiveFeedResponse, LiveFeedItemSchema

router = APIRouter()

# In-memory circular buffer for simulated and real-time live events
LIVE_FEED_STORE = [
    LiveFeedItemSchema(
        id="evt-001",
        timestamp=datetime.now(timezone.utc),
        category="APPROVAL",
        headline="FDA Approves Vertex's Suzetrigine (Journavo) for Moderate-to-Severe Acute Pain",
        ticker="VRTX",
        details="Non-opioid selective NaV1.8 inhibitor approved under priority review. First novel pain mechanism in over two decades.",
        sentiment="POSITIVE",
    ),
    LiveFeedItemSchema(
        id="evt-002",
        timestamp=datetime.now(timezone.utc),
        category="ADCOM",
        headline="FDA Advisory Committee Votes 9-2 in Favor of Sarepta's SRP-9001 Expansion",
        ticker="SRPT",
        details="Cellular, Tissue, and Gene Therapies Advisory Committee endorses broad label expansion in Duchenne muscular dystrophy.",
        sentiment="POSITIVE",
    ),
    LiveFeedItemSchema(
        id="evt-003",
        timestamp=datetime.now(timezone.utc),
        category="CRL",
        headline="FDA Issues Complete Response Letter to Lykos Therapeutics for MDMA-Assisted Therapy",
        ticker="PRIVATE",
        details="Psychopharmacologic Drugs Advisory Committee noted insufficient evidence of efficacy and study conduct concerns.",
        sentiment="NEGATIVE",
    ),
    LiveFeedItemSchema(
        id="evt-004",
        timestamp=datetime.now(timezone.utc),
        category="TRIAL_UPDATE",
        headline="Viking Therapeutics Reports Positive Phase 2b Data for VK2735 in Obesity",
        ticker="VKTX",
        details="Primary endpoint achieved with statistical significance; mean weight reduction of up to 14.7% at 13 weeks.",
        sentiment="POSITIVE",
    ),
    LiveFeedItemSchema(
        id="evt-005",
        timestamp=datetime.now(timezone.utc),
        category="8K_FILING",
        headline="Alnylam Submits sNDA for Vutrisiran in ATTR-CM Following Positive HELIOS-B Study",
        ticker="ALNY",
        details="Filing includes 28% reduction in all-cause mortality and recurrent cardiovascular events (p=0.0118).",
        sentiment="POSITIVE",
    ),
]


@router.get("/approvals/live", response_model=LiveFeedResponse)
async def get_live_approvals_feed():
    """Retrieve the latest live regulatory approvals, CRLs, and AdCom feed."""
    return LiveFeedResponse(feed=LIVE_FEED_STORE)
