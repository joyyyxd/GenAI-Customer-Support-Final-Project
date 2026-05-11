# Customer Support Reply Draft Assistant for Small Online Stores

## 1. Context, user, and problem

This project is a small GenAI workflow for small online store owners or customer support staff who need to respond to customer emails quickly and professionally.

The workflow focuses on one narrow task: drafting a first-response customer support email. The user runs the script with a customer email example as input, and the system generates a draft reply. In the improved version, the system also identifies the issue category, assigns a risk level, and indicates whether the case should be reviewed by a human.

This problem matters because small stores often do not have large support teams. Writing customer replies takes time, and poorly worded replies can create business risk, especially for refund requests, damaged-item complaints, or emotionally charged messages.

## 2. Solution and design
I built a small command-line tool for drafting first-response customer support emails. The user provides a customer support email as input. In the baseline version, the tool returns a simple draft reply. In the improved version, it returns a structured response with issue category, risk level, human review recommendation, and reply draft.

This project includes two versions of the workflow:

### Baseline
The baseline is a simple prompt-only email drafting system. It takes the customer email and generates a polite customer support reply.

### Improved system
The improved system uses a more structured prompt. The main GenAI design choices were structured output, safer prompting, and human review for risky cases.

It returns:
- issue category
- risk level
- human review recommendation
- reply draft

The improved system is designed to be safer and more useful for customer support workflows. It is instructed not to invent order details, not to promise refunds automatically, and to recommend human review for riskier messages.

### Files
- `app.py` - runs a sample customer email through the baseline and improved workflows
- `prompts.py` - stores the baseline and improved prompts
- `evaluate.py` - runs evaluation cases
- `test_cases.json` - synthetic customer support test cases
- `outputs/eval_results.txt` - saved evaluation outputs

## 3. Evaluation and results

I evaluated the system using 10 synthetic customer support emails in `test_cases.json`. These test cases cover several common situations, including:
- shipping delay
- damaged item
- refund request
- return question
- wrong item
- unclear or incomplete request
- angry complaint

The baseline and improved versions were compared on the same workflow. The improved version was designed to provide more structured and safer outputs by explicitly classifying issue type, assigning risk, and recommending human review when appropriate.

The evaluation outputs are saved in:
- `outputs/eval_results.txt`

### Criteria
I compared the improved system against the prompt-only baseline. I mainly evaluated whether: 
- the outputs were structured
- the outputs were relevant to the customer issue
- the outputs were more careful in risky case

### What worked
- The system generated polite and relevant customer support replies
- The improved version produced structured outputs
- The improved version handled refund and damaged-item cases more carefully than the baseline
- The workflow is narrow and realistic for a small business use case

### What failed or remained limited
- Free-tier API quota limits made large-batch evaluation difficult
- The model sometimes classified medium-risk cases conservatively
- The project does not connect to real order systems or store policies
- The reply is still a draft and should not be sent without human review

### What I found

Overall, the improved version produced more structured outputs and handled risky cases more carefully than the baseline, although free-tier API limits required some evaluation runs to be completed in smaller batches.

### Human involvement
A human should always review the final email before sending it. The system is meant to help draft replies, not make final refund, return, or compensation decisions.

## 4. Artifact snapshot

This repository contains a working Python-based command-line tool for customer support email drafting.

Sample input:
- Customer email: "My order was supposed to arrive three days ago, but I still have not received it."

Sample improved output:
- issue category: shipping_delay
- risk level: low
- human review needed: no
- reply draft: a polite customer support response asking for the order number and explaining that the team will investigate the shipment

Main evidence included in the repo:
- runnable code in `app.py`
- evaluation script in `evaluate.py`
- test cases in `test_cases.json`
- saved outputs in `outputs/eval_results.txt`

## 5. Setup and usage

### Requirements
Install dependencies with:

```bash
pip install -r requirements.txt
```

### (Optional) Create and activate a virtual environment before installing dependencies.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### API key

Set your Gemini API key as an environment variable before running the scripts.

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

### Run the sample app

```bash
python app.py
```

### Run evaluation

The evaluation script can be run in smaller batches if API free-tier quota limits are reached.

```bash
python evaluate.py
```

## 6. Notes

- This project uses synthetic example customer emails only
- No real customer data, secrets, or private order data are included
- The system is intended as a drafting assistant, not a fully automated support system
- Free-tier Gemini API rate limits may require running evaluation in smaller batches
- This system should not be used to make final refund, return, or compensation decisions without human review.

## 7. Lightning Presentation
[Slide Link](https://canva.link/7oj1tzbqrprmshv)