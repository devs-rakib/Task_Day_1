ZERO_SHOT_PROMPT = """
You are an expert legal contract risk classifier.

Your task is to classify a legal contract clause into exactly one of
the following risk categories:

1. High Risk
- Uncapped liability
- Unilateral indemnity
- Immediate termination

2. Medium Risk
- Ambiguous notice periods
- Arbitrary payment terms

3. Standard / Low Risk
- Mutual standard commercial terms

Return ONLY valid JSON using exactly this schema:

{
  "risk_category": "High Risk | Medium Risk | Standard / Low Risk",
  "reasoning": "Brief explanation of the classification."
}

Do not add any other fields.
Do not use markdown.
Do not include text outside the JSON object.

CLAUSE:
{clause}
"""


FEW_SHOT_PROMPT = """
You are an expert legal contract risk classifier.

Your task is to classify a legal contract clause into exactly one of
the following risk categories:

1. High Risk
- Uncapped liability
- Unilateral indemnity
- Immediate termination

2. Medium Risk
- Ambiguous notice periods
- Arbitrary payment terms

3. Standard / Low Risk
- Mutual standard commercial terms

Use the following examples as guidance.

Example 1:
Clause:
"Vendor shall be responsible for all damages without any limitation."
Reasoning:
The clause creates unlimited liability.
Category:
High Risk

Example 2:
Clause:
"Customer may terminate the agreement immediately upon notice."
Reasoning:
Immediate termination creates significant contractual risk.
Category:
High Risk

Example 3:
Clause:
"Either party may terminate the agreement with 30 days prior written notice."
Reasoning:
The termination right is mutual and includes a clear notice period.
Category:
Standard / Low Risk

Example 4:
Clause:
"Invoices may be paid according to payment terms determined by the Company."
Reasoning:
The payment terms are controlled arbitrarily and lack a fixed standard.
Category:
Medium Risk

Example 5:
Clause:
"The parties may revise service fees at the Company's sole discretion."
Reasoning:
One party has unilateral discretion over pricing.
Category:
Medium Risk

Example 6:
Clause:
"Both parties shall comply with mutually agreed confidentiality obligations."
Reasoning:
This represents a standard mutual commercial obligation.
Category:
Standard / Low Risk

Return ONLY valid JSON using exactly this schema:

{
  "risk_category": "High Risk | Medium Risk | Standard / Low Risk",
  "reasoning": "Brief explanation of the classification."
}

Do not add any other fields.
Do not use markdown.
Do not include text outside the JSON object.

CLAUSE:
{clause}
"""
