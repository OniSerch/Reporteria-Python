use polars::prelude::*;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filepath = &args[1];

    let df = CsvReader::from_path(filepath)
        .unwrap()
        .infer_schema(None)
        .has_header(true)
        .finish()
        .unwrap();

    let result = serde_json::json!({
        "rows": df.height(),
        "columns": df.width(),
        "column_names": df.get_column_names(),
    });

    println!("{}", result.to_string());
}
