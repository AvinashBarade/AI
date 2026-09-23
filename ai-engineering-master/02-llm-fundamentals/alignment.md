# Alignment

Alignment shapes behavior toward **human preferences and policies**—refusals, tone, safety, instruction following beyond bare likelihood.

## RLHF (high level)

1. SFT model
2. Train reward model from human comparisons
3. Optimize policy (PPO) to increase reward while staying close to reference

## Alternatives you’ll hear

- **DPO / IPO:** preference learning without explicit reward model training loop in some setups.
- **Constitutional AI / rules:** layer policies in training or inference.

## Production alignment is layered

Model alignment + **gateway policies** + **tool permissions** + **content filters** + **human review** for edge cases. Don’t assume the base model is your entire safety program.
