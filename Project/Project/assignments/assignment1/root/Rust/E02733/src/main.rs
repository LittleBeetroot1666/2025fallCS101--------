// Rust 语言
use std::io;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();
    if n % 4 == 0 && n % 100 != 0{
        println!("Y")
    }else if n % 400 == 0 && n % 3200 != 0 {
        println!("Y")
    }else {
        println!("N")
    }
}
