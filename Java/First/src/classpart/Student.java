package classpart;

public class Student {
	int studentId;  //학번
	String studentName;  //이름
	int grade; //학년
	String address; //주소
	
	// 학생 이름 부여
	public void setStudentName(String name) {
		studentName = name;
	}

	// 학생 이름 리턴
	public String getStudentName() {
		return studentName;
	}

	// 학생 주소 리턴
	public void showStudentInfo() {
		System.out.println(studentName + "," + address); //이름 주소 출력
	}		
		
	public static void main(String[] args) {
		Student studentAhn = new Student();
		studentAhn.studentName = "안연수";
		
		System.out.println(studentAhn.studentName);
		System.out.println(studentAhn.getStudentName());		
	}

	
}
