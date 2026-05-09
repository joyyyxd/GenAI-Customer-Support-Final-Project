# Report

## Business Use Case

This prototype focuses on a simple business writing workflow: drafting customer support email replies for a small online store. The user is a customer support assistant who receives customer emails about common order issues such as delayed shipping, damaged items, wrong items, or refund requests. The system takes a customer email as input and produces a professional first-draft response.

This workflow is a good fit for a GenAI prototype because it is repetitive, writing-heavy, and easy to evaluate using a stable set of test cases. It also has a clear business value. A support assistant can save time by using an AI-generated draft for common cases, while still reviewing or editing the draft before sending it to customers.

## Model Choice

I used the Google AI Studio Gemini API for this prototype because it was the recommended option for the assignment and it provided a simple way to make real LLM API calls from Python. After some setup issues and rate-limit errors, I was able to run the workflow successfully using gemini-3.1-flash-lite-preview, with gemini-3-flash-preview as a fallback option in the script. I chose these models because they worked with the free-tier setup and were able to generate polite, readable support email drafts.

I mainly observed two practical issues while using Gemini. First, free-tier usage sometimes caused quota and availability errors such as 429 and 503 responses. Second, even when the model worked, output quality depended heavily on prompt wording. The model was capable of producing useful drafts, but it needed clear instructions to avoid generic wording, placeholder text, and risky responses in refund-related cases.

## Baseline vs. Final Design

The baseline design used a simple prompt that asked the model to write a polite and professional first-draft reply while avoiding invented details. This initial version generally produced readable responses, but the outputs were sometimes too generic and did not clearly handle risky cases. For example, refund-related messages were answered politely, but the prompt did not strongly define how the system should respond when human review was more appropriate. In some cases, the output also used vague or template-like wording.

The first revision improved the workflow by making the prompt more specific. I added a fixed company name, removed placeholder-style language, and instructed the model not to approve refunds or invent store policies. This made the responses look more realistic and more consistent with a real business workflow. The outputs became safer and more professional, although they also became slightly more formulaic.

The final design improved the prompt again by adding clearer instructions for angry or frustrated customers. It told the model to briefly acknowledge customer frustration, avoid risky promises, and state that high-risk issues should be reviewed by the support team. This version handled emotionally charged and refund-related cases better than the baseline. Compared with the initial prompt, the final prompt produced replies that were more empathetic, more realistic, and better aligned with a human-review boundary. However, the final version also became slightly longer and more formal, even in simple cases.

Overall, prompt iteration clearly improved the system. The baseline prompt showed that the model could draft a basic support email, but the later versions made the workflow safer and more business-appropriate.

## Where the Prototype Still Fails or Requires Human Review

This prototype still should not be trusted to fully automate all support replies. It performs best on simple, low-risk cases such as shipping delays or vague complaints where the correct next step is to request more information. However, it is weaker on high-risk situations involving refund demands, angry customers, possible policy exceptions, or cases where the company would need to make a judgment call. In those cases, the model may still sound confident without actually knowing the correct policy or the full account history. For that reason, human review is still necessary whenever the message involves refunds, threats, exceptions, legal risk, or any situation where a wrong response could create customer or business harm.

## Deployment Recommendation

I would recommend deploying this workflow only in a limited way. Specifically, I would recommend it as a drafting assistant, not as a fully autonomous customer support agent. It is useful for creating a first draft in common low-risk cases, and it can save time by helping support staff respond more quickly and consistently. However, it should only be used under clear conditions: a human should review the draft before it is sent, and high-risk cases should be routed to human staff automatically.

In other words, I would recommend deployment for low-risk support drafting with human review, but I would not recommend full automation. The prototype is helpful, but the evaluation showed that safety and judgment still depend on prompt design and human oversight.