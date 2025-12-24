use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let t: usize = lines.next().unwrap().unwrap().parse().unwrap();

    for _ in 0..t {
        let n: usize = lines.next().unwrap().unwrap().parse().unwrap();
        let js: Vec<i32> = lines.next().unwrap().unwrap()
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        let ps: Vec<i32> = js.iter()
            .zip(js.iter().skip(1))
            .map(|(a, b)| (b - a).abs())
            .collect();
        let mut rs = vec![
            (js[1] - js[0]).abs(),
            (js[js.len() - 1] - js[js.len() - 2]).abs(),
        ];
        for k in 0..n-2 {
            let a = js[k];
            let b = js[k+1];
            let c = js[k+2];
            if (a > b && b < c) || (a < b && b > c) {
                let min_val = ps[k].min(ps[k+1]);
                rs.push(2 * min_val);
            }
        }
        let sum_ps: i32 = ps.iter().sum();
        let max_rs = rs.iter().max().copied().unwrap();
        println!("{}", sum_ps - max_rs);
    }
}

