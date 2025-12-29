# This is a test 

```{Python}

from fastapi import FastAPI

app = FastAPI()
```


Running the application on your computer:
```{bash}
cd adrianhredhe.com
conda activate fastapi
python -m uvicorn app.main:app --reload
```


For running conda as kernels in Molten.nvim:
```{bash}
conda create -n fastapi
conda activate fastapi
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=fastapi
```

see list of prunable kernels to do spring cleaning:
```{bash}
jupyter kernelspec list
```
