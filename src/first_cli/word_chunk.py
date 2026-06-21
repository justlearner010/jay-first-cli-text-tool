from dataclasses import dataclass
# 用argparse改写的新版本


@dataclass(init=True)
class Wordchunk:
    fname:str
    chunk_size:int

    def text_chunk(self):
        if(self.chunk_size < 0):
            print("你的文本块大小无效")
            return -1
        with open(self.fname,'r') as f:
            text = f.read()
        chunks = []
        j = 0
        for i in range(0,len(text),self.chunk_size):
            j = j+1
            chunk_data ={"chunk index":j,
                        "chunk_start":i,
                        "chunk_end":min(i+self.chunk_size,len(text)),
                        "chunk_text":text[i:i+self.chunk_size]
                        }
            chunks.append(chunk_data)

        return chunks
