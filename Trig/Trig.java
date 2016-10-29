public class Trig{
	public static double findLength(double A, double a, double B)
	{
		/* Law of Sines:
		sin(A)/a = sin(B)/b
		returns b
		*/
		return Math.sin(B)/(Math.sin(A)/a);
	}
	public static double findAngle(double A, double a, double b)
	{
		//Law of Sines; returns B
		return Math.asin(b*Math.sin(A)/a);
	}
	public static double lawCosines(double b, double c, double A)
	{
		/* Law of Cosines
		a^2 = b^2 + c^2 - b*c*cos(A)
		returns a
		*/
		return Math.sqrt((b*b) + (c*c) - (2*b*c*Math.cos(A));
	}
}
