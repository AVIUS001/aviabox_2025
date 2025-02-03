#[cfg(test)]
mod tests {
    use physics_engine::simulate_physics_step;

    #[test]
    fn test_physics_engine() {
        let (pos, vel) = simulate_physics_step(0.0, 0.0, 9.81, 1.0);
        assert!((pos - 4.905).abs() < 1e-3);
        assert!((vel - 9.81).abs() < 1e-3);
    }
}
