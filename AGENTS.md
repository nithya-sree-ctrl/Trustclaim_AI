# AGENTS.md

## TrustClaim AI - Multi-Agent Architecture

TrustClaim AI uses a collaborative multi-agent system to analyze insurance claims and verify visual evidence.

### Agent Responsibilities

### 1. Claim Agent

Purpose:

* Understand user claim description.
* Extract issue type.
* Extract damaged object.
* Generate structured claim summary.

### 2. Image Agent

Purpose:

* Analyze uploaded images.
* Detect visible damage.
* Identify damaged object parts.
* Estimate confidence score.

### 3. Evidence Agent

Purpose:

* Verify evidence requirements.
* Check minimum image count.
* Validate image quality.
* Determine evidence completeness.

### 4. Fraud Agent

Purpose:

* Analyze historical user claims.
* Detect duplicate images.
* Generate fraud risk score.
* Produce risk flags.

### 5. Severity Agent

Purpose:

* Estimate damage severity.
* Classify severity:

  * none
  * low
  * medium
  * high
  * unknown

### 6. Adjuster Agent

Purpose:

* Generate insurance recommendations.
* Recommend:

  * Approve
  * Manual Review
  * Investigate

### 7. Explainability Agent

Purpose:

* Explain decisions.
* Generate evidence-based reasoning.
* Improve transparency.

### Agent Workflow

Claim Submission
↓
Claim Agent
↓
Image Agent
↓
Evidence Agent
↓
Fraud Agent
↓
Severity Agent
↓
Adjuster Agent
↓
Explainability Agent
↓
Final Decision

## Development Rules

* No hardcoded labels.
* No hardcoded claim outcomes.
* All decisions must be generated from evidence.
* Use Gemini Vision for image understanding.
* Use explainable AI reasoning for every decision.
* Generate HackerRank-compatible output.csv.
