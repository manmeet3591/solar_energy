# Global Horizontal Irradiance (GHI) in CMIP6 Data

In the context of **CMIP6 data**, the variable `RSDS` (Surface Downward Shortwave Radiation) represents the **Global Horizontal Irradiance (GHI)**. This is because `RSDS` includes both:

1. **Direct Radiation**: Solar radiation directly reaching the surface.
2. **Diffuse Radiation**: Scattered solar radiation reaching the surface.

Thus, if you are working with `RSDS`, it already represents the total solar radiation received on a horizontal surface, which is exactly what GHI is defined as.

## Key Points
- **GHI = RSDS**: This is true if you are directly using CMIP6 data and not trying to break `RSDS` into its components.
- You only need to calculate GHI manually if you want to reconstruct it from its components:
  \[
  \text{GHI} = \text{DNI} \cdot \cos(\theta) + \text{DIF}
  \]
  Where:
  - `DNI`: Direct Normal Irradiance.
  - `cos(θ)`: Cosine of the solar zenith angle.
  - `DIF`: Diffuse Horizontal Irradiance.

## When to Use `RSDS` Directly
- If your goal is to obtain GHI from CMIP6 data without decomposing it into direct and diffuse components, you can directly use `RSDS`.
- If `RSDS` is available in your dataset, there is **no need** to calculate GHI separately unless you are performing detailed radiation modeling.

Let me know if you need further clarification or assistance with specific CMIP6 datasets!