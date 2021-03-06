pub fn build_proverb(list: &[&str]) -> String {
    match list.len() {
        0 => "".to_string(),
        _ => list.windows(2)
            .map(|win| format!("For want of a {0} the {1} was lost.", win[0], win[1]))
            .chain(std::iter::once(format!("And all for the want of a {}.",list[0])))
            .collect::<Vec<String>>()
            .join("\n") 
    }
}
