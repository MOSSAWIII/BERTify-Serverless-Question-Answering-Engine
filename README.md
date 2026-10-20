# BERTify — Serverless Question-Answering Prototype

**Python · Hugging Face Transformers · PyTorch · Docker · AWS Lambda**

A compact prototype of extractive question answering using a fine-tuned MobileBERT model and an AWS Lambda container handler. The code illustrates how an HTTP request can pass a question and context to a model and return an extracted answer.

> **Project status (October 2026):** Historic educational prototype. The repository has **not** been revalidated for deployment, accuracy, latency, scale, or security. It is **not** presented as production-ready.

## Repository map

| File | Purpose |
| --- | --- |
| [`handler.py`](handler.py) | Lambda entry point, model loading and text-answer extraction |
| [`get_model.py`](get_model.py) | Downloads the MobileBERT model and tokenizer into `./model` |
| [`dockerfile`](dockerfile) | Legacy Python 3.8 Lambda container image |
| [`requirements.txt`](requirements.txt) | Historical PyTorch / Transformers dependency pins |
| [`serverless.yml`](serverless.yml) | Historical Serverless framework deployment configuration |

## Intended flow

```text
HTTP request → API Gateway → Lambda handler
                                  ↓
                         MobileBERT + context
                                  ↓
                             JSON answer
```

The Python handler expects `event["body"]` to be a JSON string with a question and a context:

```json
{
  "question": "What does BERTify demonstrate?",
  "context": "BERTify is a demonstration of extractive question answering using a Lambda container."
}
```

Its current success response contains the extracted `answer` only. It does **not** return a measured confidence score or processing latency.

## Historical setup (not a tested quick start)

Clone the **actual** repository:

```bash
git clone https://github.com/MOSSAWIII/BERTify-Serverless-Question-Answering-Engine.git
cd BERTify-Serverless-Question-Answering-Engine
```

The code then expects a local `model/` directory. `get_model.py` downloads `mrm8488/mobilebert-uncased-finetuned-squadv2` and its tokenizer, but it relies on historical dependencies and unverified external compatibility.

**Do not run `serverless deploy` unchanged.** The committed `serverless.yml` references an account-specific ECR digest, while the Docker image and dependencies use old versions. A separate deployment refresh is required, including controlled credentials, updated dependencies, local tests and a new registry/image configuration.

## What remains unverified

- Answer accuracy, handling of impossible questions, maximum input length and model/tokenizer compatibility.
- Cold and warm latency, throughput, concurrency and operating costs.
- Authentication, rate limiting, request validation, error handling and container scanning.
- Reproducibility of model download, image build and deployment on current tooling.

This repository does **not** include a reproducible benchmark or test suite establishing these properties. No fabricated performance figures are published here.

## Future improvements

A meaningful next iteration would add a small CPU-only local test harness, pinned compatible dependencies, explicit model provenance, automated tests, an example input/output and a fresh container build. Any new performance claim should be accompanied by the measurement environment and data.

## Attribution and reuse

Model provenance: [`mrm8488/mobilebert-uncased-finetuned-squadv2`](https://huggingface.co/mrm8488/mobilebert-uncased-finetuned-squadv2). Check the model and dependency licenses separately. **No repository-level reuse license is asserted here until a license file is added.**
