use std::io;

fn main() {
    let mut ast = String::new();
    io::stdin().read_line(&mut ast).unwrap();
    let a: i32 = ast.trim().parse().unwrap();
    if a >= 4 && a % 2 == 0{
        println!("YES")
    } else { println!("NO") }
}
