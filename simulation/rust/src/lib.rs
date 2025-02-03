/// A simple physics simulation function.
pub fn simulate_physics_step(position: f64, velocity: f64, acceleration: f64, dt: f64) -> (f64, f64) {
    let new_velocity = velocity + acceleration * dt;
    let new_position = position + velocity * dt + 0.5 * acceleration * dt * dt;
    (new_position, new_velocity)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_simulate_physics_step() {
        let (pos, vel) = simulate_physics_step(0.0, 0.0, 9.81, 1.0);
        assert!((pos - 4.905).abs() < 1e-3);
        assert!((vel - 9.81).abs() < 1e-3);
    }
}
