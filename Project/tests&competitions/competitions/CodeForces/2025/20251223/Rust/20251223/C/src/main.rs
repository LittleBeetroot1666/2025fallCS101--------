use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    // 读取测试用例数量
    let t: usize = lines.next().unwrap().unwrap().parse().unwrap();

    for _ in 0..t {
        // 读取n值
        let n: usize = lines.next().unwrap().unwrap().parse().unwrap();

        // 读取数组
        let mut js: Vec<i32> = lines.next().unwrap().unwrap()
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();

        // 排序数组
        js.sort();

        // 计算结果
        let result = if n >= 2 {
            js[0].max(js[1] - js[0])
        } else {
            js[0]
        };

        println!("{}", result);
    }
}
