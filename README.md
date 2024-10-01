# **Contractual Document Chatbot with Privacy Preservation**

## **Overview**

This project addresses the problem of simplifying complex contractual documents (e.g., medical insurance, loan documents) for the general public while ensuring data privacy. The solution is implemented as a chatbot with a **Streamlit-based UI** that accepts input in the form of contractual documents and helps the user understand them in a simplified manner. Additionally, the project ensures the security of the data through an image encryption and decryption mechanism, protecting sensitive information from exposure.

The project leverages state-of-the-art machine learning techniques, including fine-tuning the **Florence-2 model** on the **DocVQA** dataset for document question answering and implementing secure encryption for sensitive document images.

**Video Demo**: [Google Drive](https://drive.google.com/file/d/1Ch9GXpYFEiHBE5ZniTLiupaMVvqb21rl/view?usp=sharing)

## **Features**

- **Streamlit UI**: A simple, user-friendly interface for document upload, question asking, and document comprehension.

- **Chatbot Interface**: Designed to answer user queries on contractual documents, such as medical insurance and loan documents, by simplifying the complex terminologies and clauses.
  
- **Privacy Preservation**: The chatbot ensures that sensitive data is not exposed, making it highly secure for users.
  
- **Fine-tuned Florence-2 Model**: The Florence-2 model has been fine-tuned on the DocVQA dataset to improve document comprehension and question answering.

- **Image Encryption/Decryption**: A robust encryption algorithm has been integrated to securely encrypt images of documents, preventing unauthorized access. Decryption ensures only authorized users can view the document.

## **Technologies Used**

- **Florence-2 Model**: [Florence: A New Vision Foundation Model](https://arxiv.org/abs/2111.11432)
- **DocVQA Dataset**: [DocVQA Dataset](https://arxiv.org/abs/2007.00398)
- **Streamlit**: For creating the interactive user interface.
- **PyTorch**: Version 2.4.1+cpu for model training and fine-tuning.
- **Image Encryption/Decryption**: Custom algorithm for secure data transmission.

## **Model Training**

The **Florence-2 model** was fine-tuned on the **DocVQA dataset** for **2 epochs** due to limited computational resources. Despite the short training time, the model showed promising results in understanding and answering questions related to contractual documents.

## **Streamlit-Based UI**

The project includes a **Streamlit UI** that allows users to:

1. **Upload Contractual Documents**: Users can upload a document (e.g., a medical insurance policy or loan agreement).
2. **Ask Questions**: The chatbot interface allows users to ask questions about the uploaded document.
3. **Receive Simplified Responses**: The chatbot provides easy-to-understand answers to complex legal terms and clauses.
4. **Encrypted Image Storage**: The document image is encrypted before being stored, ensuring privacy and security.
  
## **Image Encryption and Decryption**

A secure image encryption and decryption mechanism is included to ensure the privacy of uploaded contractual document images. This protects sensitive information from unauthorized access.

## **References**

1. Florence-2 Model: [Florence: A New Vision Foundation Model](https://arxiv.org/abs/2111.11432)
2. DocVQA Dataset: [DocVQA Dataset](https://arxiv.org/abs/2007.00398)
3. Encryption Algorithms: Research papers on encryption (add hyperlinks to specific encryption techniques/research papers you referred to).

## **Model Performance**

- The Florence-2 model was trained for 2 epochs on limited hardware resources, yielding effective results on the DocVQA dataset.
  
- Further fine-tuning with additional compute resources could further improve the model's performance in handling more diverse and complex document structures.

## **Future Enhancements**

- **Extended Model Training**: With better computational resources, extending the model training to more epochs will likely enhance document comprehension and question-answering capabilities.
  
- **Additional Features**: Future versions of the chatbot can include support for various document formats and more advanced NLP models to better address the nuances of contractual documents.
