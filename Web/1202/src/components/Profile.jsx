// Profile 컴포넌트: 사용자 프로필 정보 표시
// 객체 데이터와 배열 렌더링 예시
function Profile() {
  // 프로필 데이터를 객체로 관리
  const profile = {
    name: "김철수",
    age: 28,
    job: "프론트엔드 개발자",
    skills: ["JavaScript", "React", "TypeScript", "CSS"],
    image:
      "https://image.utoimage.com/preview/cp872722/2022/12/202212008462_500.jpg",
  };

  return (
    <div>
      {/* 기본 정보 표시 */}
      <div>
        <img src={profile.image} alt={`${profile.name}의 프로필 이미지`} />
        <h2>{profile.name}</h2>
        <p>나이: {profile.age}세</p>
        <p>직업: {profile.job}</p>
      </div>

      {/* 스킬 목록: 배열을 map으로 렌더링 */}
      <div>
        <h3>보유 스킬</h3>
        <ul>
          {profile.skills.map((skill, index) => {
            return <li key={index}>{skill}</li>;
          })}
        </ul>
      </div>
    </div>
  );
}

export default Profile;
