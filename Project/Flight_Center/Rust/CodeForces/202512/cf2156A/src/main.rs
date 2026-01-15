use std::collections::hash_set::Intersection;
use std::io;

fn main() {
    let mut t = String::new();
    io::stdin().read_line(&mut t).unwrap();
    let t: i32 = t.trim().parse().unwrap();
    for _ in 0..t {
        let mut nst = String::new();
        io::stdin().read_line( & mut nst).unwrap();
        let n: i32 = nst.trim().parse().unwrap();
        let res = (n - 1) / 2;
        println!("{}", res);
    }
}
