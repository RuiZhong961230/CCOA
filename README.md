# CCOA
Cooperative coati optimization algorithm with transfer functions for feature selection and knapsack problems

## Abstract
Coatis optimization algorithm (COA) has recently emerged as an innovative meta-heuristic algorithm (MA) for global optimization, garnering considerable attention from scholars and researchers. In this paper, we introduce three techniques to enhance COA: (1) the cooperative mechanism, (2) the fitness-based division, and (3) the optional base vector strategy. Collectively, we refer to our improved method as cooperative COA (CCOA). In addition, we introduce the incorporation of the S-shaped Sigmoid transfer function and the V-shaped Tanh transfer function into CCOA, leading to the development of SCCOA and VCCOA. These adaptations effectively address the challenges posed by feature selection tasks and the 0/1 knapsack problem. To comprehensively evaluate the performance of the continuous version of CCOA, as well as the binary versions of SCCOA and VCCOA, we conducted two distinct categories of numerical experiments. Firstly, we compared CCOA with nine representative MAs, including the original COA, on CEC2020 benchmark functions and six engineering optimization problems. Secondly, SCCOA and VCCOA are compared with six famous binary MAs on 13 feature selection datasets and 18 standard 0/1 knapsack problems. Experimental and statistical results show the competitiveness of CCOA and its binary versions, and it is promising to extend CCOA to various real-world application scenarios.

## Citation
@article{Zhong:24,  
  title={Cooperative Coati Optimization Algorithm with Transfer Functions for Feature Selection and Knapsack Problems},  
  author={Rui Zhong and Chao Zhang and Jun Yu},  
  journal={Knowledge and Information Systems},  
  pages={6933–6974},  
  volume={66},  
  year={2024},  
  publisher={Springer},  
  doi = {https://doi.org/10.1007/s10115-024-02179-3 },  
}

## Datasets and Libraries
CEC benchmarks and Engineering problems are provided by opfunu==1.0.0 and enoppy==0.1.1 libraries, respectively. ELM model and datasets in classification are provided by mafese==0.1.8 and intelelm==1.0.3 libraries.

## Contact
If you have any questions, please don't hesitate to contact zhongrui[at]iic.hokudai.ac.jp
