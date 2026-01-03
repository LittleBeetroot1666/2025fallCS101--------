use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let t: usize = lines.next().unwrap().unwrap().parse().unwrap();

    for _ in 1..=t{
        let line = lines.next().unwrap().unwrap();
        let parts: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        if (parts[0] == parts[1]) && (parts[1] == parts[2]) && (parts[2] == parts[3]) {
            println!("YES");
        }else { println!("NO"); }
    }
}
