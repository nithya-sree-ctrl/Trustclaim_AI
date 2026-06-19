CLAIM_ANALYSIS_PROMPT = """
You are an insurance claim expert.

Analyze:

1. Claim Object
2. Damaged Part
3. Issue Type
4. Severity
5. Confidence

Return JSON only.
"""

IMAGE_ANALYSIS_PROMPT = """
Analyze this image.

Return:

{
  "object_type":"",
  "damaged_part":"",
  "issue_type":"",
  "severity":"",
  "confidence":""
}
"""

FRAUD_ANALYSIS_PROMPT = """
Analyze claim for fraud indicators.

Return:

{
  "fraud_score":"",
  "risk_flags":[]
}
"""