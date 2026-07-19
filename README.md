# SVHalluc: Benchmarking Speech–Vision Hallucination in Audio-Visual Large Language Models

> **TL;DR:** Speech content is not necessarily visual evidence. **SVHalluc** tests whether audio-visual large language models (AV-LLMs) can distinguish what is *said* from what is actually *seen*.

SVHalluc is introduced in **“SVHalluc: Benchmarking Speech–Vision Hallucination in Audio-Visual Large Language Models,” CVPR 2026**.

[Project Page](https://chenshuang-zhang.github.io/projects/svhalluc/) · [Paper](https://arxiv.org/abs/2606.02642) · [Dataset](https://huggingface.co/datasets/zcs15/SVHalluc)

## Contact

For any questions about the dataset or code, please contact **Chenshuang Zhang** ([chenshuang.zhang02@gmail.com](mailto:chenshuang.zhang02@gmail.com)).

## Motivation

Existing audio-visual hallucination benchmarks commonly treat environmental sounds, such as a dog barking, as evidence that an event occurred. Human speech is fundamentally different: it carries dense semantic content and may refer to past, present, or future events. An AV-LLM may recognize speech correctly while still incorrectly assuming that the spoken content is visible.

SVHalluc evaluates this failure mode from two complementary perspectives:

- **Semantic hallucination:** What content mentioned in speech is supported by the video?
- **Temporal hallucination:** When does the narrated event happen visually?

## Benchmark Overview

SVHalluc contains **2,405 video–question pairs** associated with **872 unique videos**. It includes **1,422 semantic samples** and **983 temporal samples** across six diagnostic tasks.

| Category | Task | Abbreviation | Description |
|---|---|---:|---|
| Semantic | Global Semantic Alignment | GSA | Video-level semantic matching between speech and visual events |
| Semantic | Fine-grained Semantic Alignment | FGSA | Object-level semantic grounding |
| Semantic | Cross-Modal Semantic Binding | CSMB | Event-level semantic grounding |
| Temporal | Temporal Alignment | TA | Whether the narrated and visual events occur at the same time |
| Temporal | Temporal Forecasting | TF | Whether the event occurs in the past, present, or future relative to speech |
| Temporal | Cross-Modal Temporal Binding | CMTB | Which visual action occurs when the speech is heard |

## Get the Dataset

The videos and annotations are hosted on the [Hugging Face Hub](https://huggingface.co/datasets/zcs15/SVHalluc). 

Install the dependency and download the complete dataset:

```bash
python -m pip install -r requirements.txt
python dataset/download_dataset.py --output-dir ./data/SVHalluc
```

## Data Format

After downloading, the dataset is organized as follows:

```text
data/SVHalluc/
├── README.md
├── samples.json
├── semantic/
│   └── .../*.mp4
└── temporal/
    └── .../*.mp4
```

`samples.json` is a JSON list in which each object is one video–question pair:

```json
{
  "video_path": "semantic/119/wqpqx-Qm7lk/e4714d74c73bbe3b.mp4",
  "data_type": "semantic",
  "task_type": "Global Semantic Alignment",
  "task_type_abbr": "GSA",
  "question": "Does the speech describe the visual events in the video? (A) Yes (B) No",
  "answer": "B"
}
```

| Field | Type | Description |
|---|---|---|
| `video_path` | string | MP4 path relative to the downloaded dataset root |
| `data_type` | string | `semantic` or `temporal` |
| `task_type` | string | Full task name |
| `task_type_abbr` | string | `GSA`, `FGSA`, `CSMB`, `TA`, `TF`, or `CMTB` |
| `question` | string | Multiple-choice question with answer options |
| `answer` | string | Correct option letter (`A`, `B`, or `C`) |

Multiple questions can reference the same video. Use `video_path`, rather than the row index, as the video identifier.

## Load with Python

```python
import json
from pathlib import Path

root = Path("data/SVHalluc")
samples = json.loads((root / "samples.json").read_text(encoding="utf-8"))

sample = samples[0]
video_path = root / sample["video_path"]
question = sample["question"]
answer = sample["answer"]
```

## Evaluation

SVHalluc is a multiple-choice benchmark. A model receives the video, including audio, and the question exactly as stored in `samples.json`. Compare the predicted option letter against `answer` and report accuracy for each task.


## License and Usage Terms

The benchmark annotations and underlying videos may be governed by different terms. The dataset is based on YouCook2 and source YouTube videos. Users are responsible for complying with the applicable SVHalluc, YouCook2, YouTube, and source-video terms before downloading, redistributing, or using the data.

The dataset is provided for research purposes. No ownership of third-party video content is transferred by this release. See [LICENSE_NOTICE.md](LICENSE_NOTICE.md) for details.

## Citation

If you find SVHalluc useful, please cite:

```bibtex
@InProceedings{Zhang_2026_SVHalluc,
  author    = {Chenshuang Zhang and Kyeong Seon Kim and Chengxin Liu and Tae-Hyun Oh},
  title     = {SVHalluc: Benchmarking Speech--Vision Hallucination in Audio-Visual Large Language Models},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  month     = {June},
  year      = {2026}
}
```

