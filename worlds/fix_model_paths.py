import argparse
import os
import os.path as osp

def main(args):
    for fname in os.listdir(args.root):
        path = osp.join(args.root, fname)
        if osp.isdir(path) and osp.exists(osp.join(path, "model.sdf")):
            with open(osp.join(path, "model.sdf"), "r") as fin, open("temp.txt", "w") as fout:
                for line in fin:
                    line = line.replace("file://models", "model://")
                    fout.write(line)
            os.rename("temp.txt", osp.join(path, "model.sdf"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=str)

    args = parser.parse_args()
    main(args)
