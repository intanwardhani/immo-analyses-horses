from file_utils import FileManager

def main():
    fm = FileManager()                
    df = fm.get_csv("~/data/properties_data_original.csv")
    print(df)

if __name__ == "__main__":
    main()

