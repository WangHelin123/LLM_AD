CUDA_VISIBLE_DEVICES=1 OPENAI_API_KEY="OpenAi Key" python eval_gpt_review.py \
    --question \
    /path/to/LLaVA/AD/124data_question.jsonl \
    --answer-list \
    /path/to/LLaVA/AD/124_chosen_ref.jsonl \
    /path/to/LLaVA/AD/Result/124data_answer.jsonl \
    --rule \
    /path/to/LLaVA/llava/eval/table/rule.json \
    --output \
    /path/tp/LLaVA/AD/Review/124_data_review.json
