use std::io;

fn main(){
    let mut k = String::new();
    io::stdin().read_line(&mut k).unwrap();
    let k: i32 = k.trim().parse().unwrap();
    let mut l = String::new();
    io::stdin().read_line(&mut l).unwrap();
    let l: i32 = l.trim().parse().unwrap();
    let mut m = String::new();
    io::stdin().read_line(&mut m).unwrap();
    let m: i32 = m.trim().parse().unwrap();
    let mut n = String::new();
    io::stdin().read_line(&mut n).unwrap();
    let n: i32 = n.trim().parse().unwrap();
    let mut d = String::new();
    io::stdin().read_line(&mut d).unwrap();
    let d: i32 = d.trim().parse().unwrap();
    let mut  cnt = 0;
    for i in 1..=d{
        if i % k ==0 || i % l == 0 || i % m == 0 || i % n == 0{
            cnt += 1
        }
    }
    println!("{}",cnt);
}
