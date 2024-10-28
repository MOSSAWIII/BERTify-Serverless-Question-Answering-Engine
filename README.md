# 🧠 BERTify: Serverless Question-Answering Engine

[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange.svg)](https://aws.amazon.com/lambda/)
[![HuggingFace](https://img.shields.io/badge/🤗-Transformers-yellow.svg)](https://huggingface.co/transformers)
[![Docker](https://img.shields.io/badge/Docker-Container-blue.svg)](https://www.docker.com/)
[![Serverless](https://img.shields.io/badge/Serverless-Framework-red.svg)](https://www.serverless.com/)
[![Python 3.8](https://img.shields.io/badge/Python-3.8-green.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

<p align="center">
  <img src="/api/placeholder/800/400" alt="BERTify Architecture" width="800"/>
</p>

Transform any text into intelligent answers with enterprise-grade NLP. BERTify combines the power of BERT language models with serverless architecture to deliver lightning-fast, scalable question-answering capabilities.

## 🌟 Why BERTify?

- **Zero Infrastructure Management**: Fully serverless architecture on AWS Lambda
- **Production-Ready Performance**: ~220ms response time for warm invocations
- **Enterprise Scalability**: Auto-scales to thousands of concurrent requests
- **Cost-Effective**: Pay only for actual usage, no idle servers
- **Modern Tech Stack**: Docker + AWS Lambda + HuggingFace Transformers

## 🚀 Quick Start

### Prerequisites

```bash
# Install required tools
npm install -g serverless
pip install aws-cli
# Configure AWS credentials
aws configure
```

### Deploy Your Own Instance

```bash
# Clone the repository
git clone https://github.com/MOSSAWIII/bertify
cd bertify

# Download BERT model
python3 get_model.py

# Build and deploy
docker build -t bertify .
serverless deploy
```

## 💡 Usage Example

```python
import requests
import json

API_ENDPOINT = "https://your-api-url/qa"

# Example question
payload = {
    "context": """
    BERTify is a serverless question-answering engine that leverages 
    BERT language models to provide instant answers from any given text. 
    It can handle thousands of concurrent requests with sub-second latency.
    """,
    "question": "What is BERTify's main capability?"
}

# Send request
response = requests.post(API_ENDPOINT, json=payload)
answer = response.json()['answer']
print(f"Answer: {answer}")
```

## 🔧 Architecture

<p align="center">
  <img src="/api/placeholder/800/400" alt="BERTify Architecture" width="800"/>
</p>

1. **API Gateway** receives HTTPS requests
2. **AWS Lambda** with custom Docker container processes requests
3. **BERT Model** performs question-answering inference
4. **Auto-scaling** handles traffic spikes seamlessly

## 📊 Performance Metrics

| Metric | Value |
|--------|--------|
| Cold Start | ~6.7s |
| Warm Response | ~220ms |
| Max Concurrent Requests | Auto-scaling |
| Memory Usage | 5GB |
| Max Context Length | 512 tokens |

## 🛠️ Configuration

Customize your deployment in `serverless.yml`:

```yaml
provider:
  name: aws
  region: eu-central-1
  memorySize: 5120
  timeout: 30

functions:
  questionanswering:
    image: ${ECR_IMAGE_URL}
    events:
      - http:
          path: qa
          method: post
```

## 📘 API Documentation

### POST /qa

```json
{
  "context": "Your text content here...",
  "question": "Your question about the context..."
}
```

Response:
```json
{
  "answer": "Extracted answer from context",
  "confidence": 0.95,
  "latency": "123ms"
}
```

## 🔒 Security

- API Gateway authentication support
- AWS IAM role-based access control
- Docker container security scanning
- Input validation and sanitization

## 🌐 Use Cases

- **Customer Support**: Automate FAQ responses
- **Document Analysis**: Extract insights from large documents
- **Research**: Analyze scientific papers and reports
- **Education**: Create interactive learning systems
- **Content Management**: Enhance content search and retrieval

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🧪 Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=MOSSAWIII/bertify&type=Date)](https://star-history.com/#MOSSAWIII/bertify&Date)

## 👤 Author

**Mohamed Amine EL MOUSSAOUI**  
ML Engineer & Cloud Architecture Specialist

[![GitHub Follow](https://img.shields.io/github/followers/MOSSAWIII?style=social)](https://github.com/MOSSAWIII)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/medaminelmoussaoui/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <a href="https://github.com/MOSSAWIII/bertify/issues">Report Bug</a> ·
  <a href="https://github.com/MOSSAWIII/bertify/issues">Request Feature</a>
</p>

<p align="center">If you find this project useful, please consider giving it a ⭐️!</p>