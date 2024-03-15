from pathlib import Path
import ray 

ray.init()
# Ray dataset
EFS_DIR = "/Users/gauravkungwani/Downloads/langchain_crash_course/langchain"
DOCS_DIR = Path(EFS_DIR, "toc_notifications_2023_1991")
ds = ray.data.from_items([{"path": path} for path in DOCS_DIR.rglob("*.html") 
if not path.is_dir()])
print(f"{ds.count()} documents")