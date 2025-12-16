import React, { useEffect, useState } from "react";

export default function SearchResults() {
  const [searchTerm, setSearchTerm] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  //   searchTerm이 변경될 때만 실행
  useEffect(() => {
    if (!searchTerm) {
      setResults([]);
      return;
    }
    console.log(`${searchTerm} 검색 중...`);

    setLoading(true);

    const database = [
      { id: 1, name: "Apple" },
      { id: 2, name: "Banana" },
      { id: 3, name: "Orange" },
      { id: 4, name: "Grape" },
    ];

    const filtered = database.filter((item) => {
      return item.name
        .toLocaleLowerCase()
        .includes(searchTerm.toLocaleLowerCase());
    });

    setResults(filtered);
    setLoading(false);
  }, [searchTerm]);

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="과일 이름 검색"
      />

      {loading && <p>검색중...</p>}

      <ul>
        {results.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}
