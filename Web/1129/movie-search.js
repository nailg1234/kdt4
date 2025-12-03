/**
 * 영화 검색 앱 - TMDB API 활용
 *
 * 주요 기능:
 * 1. 영화 제목으로 검색
 * 2. 인기 영화 목록 표시 (페이지네이션)
 * 3. 영화 상세 정보 모달
 * 4. 포스터 및 배경 이미지 표시
 */

// API 설정
const BASE_URL = "https://api.themoviedb.org/3";
const API_KEY = "d40653d9f45c0c0a68900733a9c2b6e7";
const IMG_BASE = "https://image.tmdb.org/t/p";

// 현재 페이지 번호
let currentPage = 1;

// DOM 요소 선택
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const message = document.getElementById("message");
const searchResults = document.getElementById("searchResults");
const searchMovieList = document.getElementById("searchMovieList");
const popularMovies = document.getElementById("popularMovies");
const popularMovieList = document.getElementById("popularMovieList");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const pageInfo = document.getElementById("pageInfo");
const modal = document.getElementById("modal");
const closeModal = document.getElementById("closeModal");
const modalBody = document.getElementById("modalBody");

/**
 * 이미지 URL 생성 함수
 * @param {string} path - 이미지 경로
 * @param {string} size - 이미지 크기 (w500, original 등)
 * @returns {string} 완성된 이미지 URL
 */
function getImageUrl(path, size = "w500") {
  return path
    ? `${IMG_BASE}/${size}${path}`
    : "https://via.placeholder.com/500x750?text=No+Image";
}

/**
 * 인기 영화 목록을 가져오는 함수
 * @param {number} page - 페이지 번호
 */
async function getPopularMovies(page = 1) {
  try {
    const response = await fetch(
      `${BASE_URL}/movie/popular?api_key=${API_KEY}&language=ko-KR&page=${page}`
    );

    if (!response.ok) {
      throw new Error("영화 정보를 가져오는데 실패했습니다.");
    }

    const data = await response.json();
    console.log(`인기 영화 (페이지 ${page}):`, data);

    // 영화 목록 표시
    displayMovies(data.results, popularMovieList);

    // 페이지 정보 업데이트
    currentPage = page;
    updatePagination(data.page, data.total_pages);

    return data;
  } catch (error) {
    console.error("인기 영화 조회 오류:", error);
    showMessage("인기 영화를 불러오는데 실패했습니다.", "error");
  }
}

/**
 * 영화를 검색하는 함수
 * @param {string} query - 검색어
 */
async function searchMovies(query) {
  try {
    hideMessage();

    const response = await fetch(
      `${BASE_URL}/search/movie?api_key=${API_KEY}&language=ko-KR&query=${encodeURIComponent(
        query
      )}`
    );

    if (!response.ok) {
      throw new Error("영화 검색에 실패했습니다.");
    }

    const data = await response.json();
    console.log("검색 결과:", data);

    // 검색 결과가 없는 경우
    if (data.results.length === 0) {
      showMessage("검색 결과가 없습니다. 다른 제목으로 검색해보세요.", "info");
      hideSearchResults();
      return;
    }

    // 검색 결과 표시
    displayMovies(data.results, searchMovieList);
    showSearchResults();
    hidePopularMovies();

    return data;
  } catch (error) {
    console.error("영화 검색 오류:", error);
    showMessage("영화 검색에 실패했습니다.", "error");
  }
}

/**
 * 영화 상세 정보를 가져오는 함수
 * @param {number} movieId - 영화 ID
 */
async function getMovieDetails(movieId) {
  try {
    const response = await fetch(
      `${BASE_URL}/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`
    );

    if (!response.ok) {
      throw new Error("영화 상세 정보를 가져오는데 실패했습니다.");
    }

    const movie = await response.json();
    console.log("영화 상세 정보:", movie);

    // 모달에 상세 정보 표시
    displayMovieDetails(movie);

    return movie;
  } catch (error) {
    console.error("영화 상세 정보 조회 오류:", error);
    alert("영화 상세 정보를 불러오는데 실패했습니다.");
  }
}

/**
 * 영화 목록을 화면에 표시하는 함수
 * @param {Array} movies - 영화 배열
 * @param {HTMLElement} container - 영화를 표시할 컨테이너
 */
function displayMovies(movies, container) {
  container.innerHTML = movies
    .map(
      (movie) => `
      <div class="movie-card" onclick="getMovieDetails(${movie.id})">
        <img src="${getImageUrl(movie.poster_path)}" alt="${movie.title}" />
        <div class="movie-info">
          <h3 class="movie-title">${movie.title}</h3>
          <div class="movie-meta">
            <span class="rating">⭐ ${movie.vote_average.toFixed(1)}</span>
            <span class="release-date">${
              movie.release_date || "미정"
            }</span>
          </div>
        </div>
      </div>
    `
    )
    .join("");
}

/**
 * 영화 상세 정보를 모달에 표시하는 함수
 * @param {Object} movie - 영화 상세 정보 객체
 */
function displayMovieDetails(movie) {
  modalBody.innerHTML = `
    <div class="movie-detail">
      <!-- 배경 이미지 -->
      ${
        movie.backdrop_path
          ? `<div class="backdrop" style="background-image: url('${getImageUrl(
              movie.backdrop_path,
              "original"
            )}')"></div>`
          : ""
      }

      <!-- 영화 정보 -->
      <div class="detail-content">
        <div class="detail-main">
          <!-- 포스터 -->
          <img class="detail-poster" src="${getImageUrl(
            movie.poster_path
          )}" alt="${movie.title}" />

          <!-- 정보 -->
          <div class="detail-info">
            <h2>${movie.title}</h2>
            ${
              movie.original_title !== movie.title
                ? `<p class="original-title">${movie.original_title}</p>`
                : ""
            }

            <div class="detail-meta">
              <span class="rating">⭐ ${movie.vote_average.toFixed(
                1
              )}</span>
              <span>${movie.release_date || "미정"}</span>
              <span>${movie.runtime ? `${movie.runtime}분` : ""}</span>
            </div>

            <div class="genres">
              ${movie.genres
                .map((genre) => `<span class="genre-tag">${genre.name}</span>`)
                .join("")}
            </div>

            <div class="overview">
              <h3>줄거리</h3>
              <p>${movie.overview || "줄거리 정보가 없습니다."}</p>
            </div>

            ${
              movie.homepage
                ? `<a href="${movie.homepage}" target="_blank" class="homepage-btn">공식 홈페이지 방문</a>`
                : ""
            }
          </div>
        </div>
      </div>
    </div>
  `;

  // 모달 표시
  modal.style.display = "flex";
}

/**
 * 페이지네이션 버튼 상태 업데이트
 * @param {number} page - 현재 페이지
 * @param {number} totalPages - 전체 페이지 수
 */
function updatePagination(page, totalPages) {
  pageInfo.textContent = `페이지 ${page}`;
  prevBtn.disabled = page <= 1;
  nextBtn.disabled = page >= totalPages;
}

/**
 * 메시지 표시
 * @param {string} text - 메시지 내용
 * @param {string} type - 메시지 타입 (error, info)
 */
function showMessage(text, type = "info") {
  message.textContent = text;
  message.className = `message ${type}`;
  message.style.display = "block";
}

/**
 * 메시지 숨김
 */
function hideMessage() {
  message.style.display = "none";
}

/**
 * 검색 결과 영역 표시
 */
function showSearchResults() {
  searchResults.style.display = "block";
}

/**
 * 검색 결과 영역 숨김
 */
function hideSearchResults() {
  searchResults.style.display = "none";
}

/**
 * 인기 영화 영역 숨김
 */
function hidePopularMovies() {
  popularMovies.style.display = "none";
}

/**
 * 인기 영화 영역 표시
 */
function showPopularMovies() {
  popularMovies.style.display = "block";
}

/**
 * 검색 버튼 클릭 핸들러
 */
function handleSearch() {
  const query = searchInput.value.trim();

  // 입력값 검증
  if (!query) {
    showMessage("영화 제목을 입력해주세요.", "error");
    return;
  }

  // 영화 검색
  searchMovies(query);
}

/**
 * 초기 화면으로 돌아가기
 */
function resetToHome() {
  searchInput.value = "";
  hideSearchResults();
  hideMessage();
  showPopularMovies();
  getPopularMovies(currentPage);
}

// === 이벤트 리스너 등록 ===

// 검색 버튼 클릭
searchBtn.addEventListener("click", handleSearch);

// Enter 키로 검색
searchInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    handleSearch();
  }
});

// 검색 입력이 비어있으면 초기 화면으로
searchInput.addEventListener("input", (e) => {
  if (!e.target.value.trim() && searchResults.style.display === "block") {
    resetToHome();
  }
});

// 이전 페이지 버튼
prevBtn.addEventListener("click", () => {
  if (currentPage > 1) {
    getPopularMovies(currentPage - 1);
  }
});

// 다음 페이지 버튼
nextBtn.addEventListener("click", () => {
  getPopularMovies(currentPage + 1);
});

// 모달 닫기 버튼
closeModal.addEventListener("click", () => {
  modal.style.display = "none";
});

// 모달 바깥 클릭 시 닫기
modal.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
  }
});

// ESC 키로 모달 닫기
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && modal.style.display === "flex") {
    modal.style.display = "none";
  }
});

// 페이지 로드 시 인기 영화 목록 표시
window.addEventListener("DOMContentLoaded", () => {
  getPopularMovies(1);
});
