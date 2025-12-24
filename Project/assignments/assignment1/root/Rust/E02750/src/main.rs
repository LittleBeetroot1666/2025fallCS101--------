// Rust 语言
use std::io;

fn main() {
    let mut a = String::new();
    io::stdin().read_line(&mut a).unwrap();
    let a: i32 = a.trim().parse().unwrap();
    if a % 2 == 0 {
        println!("{} {}", (a + 2) / 4, a / 2);
    }else {
        println!("0 0");
    }
}
