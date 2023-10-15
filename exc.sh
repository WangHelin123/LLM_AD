CUDA_VISIBLE_DEVICES=1 /home/yifan/miniconda3/envs/llava/bin/python model_vqa.py \
    --model-path /path/to/llava \
    --question-file \
    /path/to/LLaVA/AD/124data_question.jsonl \
    --image-folder \
    /path/to/LLaVA/124_data_image \
    --answers-file \
    /path/to/LLaVA/AD/Result/124data_answer.jsonl \
