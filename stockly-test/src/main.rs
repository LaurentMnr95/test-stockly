use std::collections::HashMap;
use std::collections::VecDeque;
use std::io;
use std::str::FromStr;
fn read_line() -> String {
    let mut buffer = String::new();
    io::stdin()
        .read_line(&mut buffer)
        .expect("failed to read line");

    buffer
}

fn read<T: FromStr>() -> Result<T, T::Err> {
    read_line().trim().parse::<T>()
}

fn read_vec<T: FromStr>() -> Result<Vec<T>, T::Err> {
    read_line()
        .split_whitespace()
        .map(|x| x.parse::<T>())
        .collect()
}

fn compute_graph(_nb_intersections: i32, _shortcuts: &Vec<i32>) -> HashMap<i32, Vec<i32>> {
    let mut graph_result = HashMap::<i32, Vec<i32>>::new();
    let mut i: i32 = 1;

    // i = 1 particular case
    let path = Vec::<i32>::from([i + 1, _shortcuts[i as usize - 1]]);
    graph_result.insert(i as i32, path);
    i += 1;

    // general case
    while i < _nb_intersections {
        let path = Vec::<i32>::from([i - 1, i + 1 as i32, _shortcuts[i as usize - 1]]);
        graph_result.insert(i as i32, path);
        i += 1;
    }

    let path = Vec::<i32>::from([i - 1, _shortcuts[i as usize - 1]]);
    graph_result.insert(i as i32, path);

    graph_result
}

fn compute_solution(graph: &HashMap<i32, Vec<i32>>) -> Vec<i32> {
    let mut next_to_visit = VecDeque::<i32>::new();
    let mut depth: HashMap<i32, i32> = HashMap::with_capacity(graph.len());
    for i in graph.keys() {
        depth.insert(*i, 10000000);
    }

    next_to_visit.push_back(1 as i32);
    depth.insert(1 as i32, 0);

    while next_to_visit.len() > 0 {
        let node = next_to_visit.pop_front().unwrap();
        let to_visit = graph.get(&node).unwrap();

        for child in to_visit {
            let curr_depth_child = depth[&child];
            if curr_depth_child == 10000000 {
                next_to_visit.push_back(*child);
                depth.insert(*child, depth[&node] + 1);
            }
        }
    }

    let mut solution_vec = vec![0; graph.len()];

    for i in graph.keys() {
        solution_vec[*i as usize - 1] = *depth.get(&i).unwrap()
    }
    solution_vec
}

fn main() {
    let nb_intersections = read::<i32>().unwrap();
    let shortcuts = read_vec::<i32>().unwrap();
    let graph = compute_graph(nb_intersections, &shortcuts);
    let solution = compute_solution(&graph);
    let str_solution: String = solution.iter().map(|&id| id.to_string() + " ").collect();
    println!("{}", str_solution);
}
