use std::io;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();
    if n == 0 {
        println!("{}",0);
    } else {
        println!("{}",1);
    }
}
