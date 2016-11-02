public class Trig{
	public static double findLength(double A, double a, double B)
	{
		/*
         * Law of Sines:
         * for any angle/side length pairs (A, a) and (B, b) the following holds:
		 * sin(A)/a = sin(B)/b
		 * returns b
		 */
		return Math.sin(B)/(Math.sin(A)/a);
	}
	public static double findAngle(double A, double a, double b)
	{
		//Law of Sines ^ returns B
		return Math.asin(b*Math.sin(A)/a);
	}
	public static double lawCosines(double b, double c, double A)
	{
		/*
         * Law of Cosines.
         * Given any triangle with side length a, opposite angle A, and other
         * side lengths b and c, the following holds
		 * a^2 = b^2 + c^2 - b*c*cos(A)
		 * This figures out a, given A, b, and c
		 */
		return Math.sqrt((b*b) + (c*c) - (2*b*c*Math.cos(A));
	}
}
