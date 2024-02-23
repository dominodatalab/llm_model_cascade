# LLM_Model_Cascade

## About this project
This project is a Langchain implementation of [Large Language Model Cascades with Mixture of Thoughts Representations for Cost-efficient Reasoning](https://arxiv.org/pdf/2310.03094.pdf) with some differences. In addition to the methods mentioned in the paper, this project also includes an implementation of Tree of Thought that can be used to sample answers. The comparisons for the vote based method and the verification based method use embedding distances and we do not include examples for in-context demonstrations, however these can be added by simply changing the prompt templates in the code.

The assets available in this project are:

*model_cascade.ipynb* - This notebook includes all the code necessary to run the methods detailed in the paper mentioned above.


## Set up instructions

This project requires the following [compute environments](https://docs.dominodatalab.com/en/latest/user_guide/f51038/environments/) to be present. Please ensure the "Automatically make compatible with Domino" checkbox is selected while creating the environment.

### Hardware Requirements
You also need to make sure that the hardware tier running the notebook or the fine-tuning script has sufficient resources. A GPU with >=16GB of VRAM is recommended. This project was tested on a `V100` with **16GB** VRAM. Also note that the model binary occupies ~ **28GB** on disc so please provision your workspace volume accordingly.

### Environment Requirements

**Environment Base**

***base image :*** `5.9 Domino Standard Environment - ubuntu20-py3.9-r4.3`

Any DSE with Python 3.9 will also work

***Dockerfile instructions***
```
RUN pip install langchain==0.1.8 langchain-openai==0.0.5 langchain-experimental==0.0.52 sentence-transformers==2.3.1 ipywidgets
```
***Pluggable Workspace Tools** 
```
jupyterlab:
  title: "JupyterLab"
  iconUrl: "/assets/images/workspace-logos/jupyterlab.svg"
  start: [  "/opt/domino/workspaces/jupyterlab/start" ]
  httpProxy:
    internalPath: "/{{ownerUsername}}/{{projectName}}/{{sessionPathComponent}}/{{runId}}/{{#if pathToOpen}}tree/{{pathToOpen}}{{/if}}"
    port: 8888
    rewrite: false
    requireSubdomain: false
```
Please change the value in `start` according to your Domino version.
