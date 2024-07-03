from setuptools import setup, find_packages

setup(
    name='RAG_Project',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'transformers==4.41.2',
        'bitsandbytes==0.43.1',
        'accelerate==0.31.0',
        'langchain==0.2.5',
        'langchainhub==0.1.20',
        'langchain-chroma==0.1.1',
        'langchain-community==0.2.5',
        'langchain_huggingface==0.0.3',
        'python-dotenv==1.0.1',
        'pypdf==4.2.0',
        'numpy==1.24.4',
        'chainlit==1.1.304',
        'localtunnel',
        'streamlit',
    ],
)
