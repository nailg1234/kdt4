function Profile() {
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
      <div>
        <img src={profile.image} alt={`${profile.name}의 프로필 이미지`} />
        <h2>{profile.name}</h2>
        <p>나이: {profile.age}세</p>
        <p>직업: {profile.job}</p>
      </div>

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
