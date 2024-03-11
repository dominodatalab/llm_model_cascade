# LLM_Model_Cascade

## About this project
This project is a Langchain implementation of [Large Language Model Cascades with Mixture of Thoughts Representations for Cost-efficient Reasoning](https://arxiv.org/pdf/2310.03094.pdf) with some differences. In addition to the methods mentioned in the paper, this project also includes an implementation of Tree of Thought that can be used to sample answers. The comparisons for the vote based method and the verification based method use embedding distances and we do not include examples for in-context demonstrations, however these can be added by simply changing the prompt templates in the code.

The assets available in this project are:

*model_cascade.ipynb* - This notebook includes all the code necessary to run the methods detailed in the paper mentioned above.

Additionally, an accompanying blog post about MoT is available at [Navigating Cost-Complexity: Mixture of Thought LLM Cascades Illuminate a Path to Efficient Large Language Model Deployment](https://towardsdatascience.com/navigating-cost-complexity-mixture-of-thought-llm-cascades-illuminate-a-path-to-efficient-large-23291d1eda41)


## Set up instructions

This project requires the following [compute environments](https://docs.dominodatalab.com/en/latest/user_guide/f51038/environments/) to be present. Please ensure the "Automatically make compatible with Domino" checkbox is selected while creating the environment.

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
