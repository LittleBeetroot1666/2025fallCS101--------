use std::io;

fn main() {
    let ast = String::new();
    let a: i32 = ast.trim().parse().unwrap();
    if a >= 4 && a % 2 == 0{
        println!("Yes");
    } else { println!("NO"); }
}

