from ingestion import read_file

def test_read_csv(tmp_path):
    file = tmp_path/"sensor.csv"
    file.write_text("temperature,pressure\n25,100")
    data = read_file(tmp_path)

    assert len(data)==1
    assert list(data.columns) == ["temperature", "pressure"]
