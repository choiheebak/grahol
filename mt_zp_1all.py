import streamlit as st
import datetime
import os

def Crawler(game):

    if game == "s":

        def save_post(content, post_id=None):
            if post_id is None:
                post_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            
            posts = load_posts()
            if post_id:
                posts = [post for post in posts if post[0] != post_id]
            posts.append((post_id, content))
            
            with open("soccer_posts.txt", "w") as f:
                for pid, cont in posts:
                    f.write(f"{pid}|{cont}\n")

        def load_posts():
            posts = []
            if os.path.exists("soccer_posts.txt"):
                with open("soccer_posts.txt", "r") as f:
                    for line in f:
                        parts = line.strip().split("|", 1)
                        if len(parts) == 2:
                            post_id, content = parts
                            posts.append((post_id, content))
            
            # 날짜를 기준으로 내림차순 정렬
            posts.sort(key=lambda x: x[0], reverse=True)
            return posts

        def delete_post(post_id):
            posts = load_posts()
            posts = [post for post in posts if post[0] != post_id]
            with open("soccer_posts.txt", "w") as f:
                for pid, cont in posts:
                    f.write(f"{pid}|{cont}\n")

        st.title("축구 게시판")

        st.markdown(":red[자유롭게 게시할 수 있자만, 욕설과 비방은 삼가해 주세요. 자기의 닉네임을 게시글에 작성하면 본인 표시가 됩니다. 작성후 목록에서 수정과 삭제가 가능합니다.]")

        # 게시글 작성
        new_post = st.text_area("새 게시글 작성 ")
        if st.button("게시"):
            save_post(new_post)
            st.success("게시글이 저장되었습니다.")
            st.rerun()

        # 게시글 목록 표시 및 수정/삭제 기능
        st.subheader("게시글 목록")
        posts = load_posts()
        if not posts:
            st.info("게시된 글이 없습니다.")
        else:
            for post_id, content in posts:
                st.write(f"ID: {post_id}")
                st.write(content)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("수정", key=f"edit_button_{post_id}"):
                        st.session_state[f'edit_mode_{post_id}'] = True
                
                with col2:
                    if st.button("삭제", key=f"delete_{post_id}"):
                        delete_post(post_id)
                        st.success("게시글이 삭제되었습니다.")
                        st.rerun()

                if f'edit_mode_{post_id}' in st.session_state and st.session_state[f'edit_mode_{post_id}']:
                    edited_content = st.text_area("수정할 내용", content, key=f"edit_{post_id}")
                    if st.button("수정 완료", key=f"edit_complete_{post_id}"):
                        save_post(edited_content, post_id)
                        st.success("게시글이 수정되었습니다.")
                        del st.session_state[f'edit_mode_{post_id}']
                        st.rerun()
                    if st.button("취소", key=f"edit_cancel_{post_id}"):
                        del st.session_state[f'edit_mode_{post_id}']
                        st.rerun()

                st.markdown("---")

    elif game == "b":

        def save_post(content, post_id=None):
            if post_id is None:
                post_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            
            posts = load_posts()
            if post_id:
                posts = [post for post in posts if post[0] != post_id]
            posts.append((post_id, content))
            
            with open("baseball_posts.txt", "w") as f:
                for pid, cont in posts:
                    f.write(f"{pid}|{cont}\n")

        def load_posts():
            posts = []
            if os.path.exists("baseball_posts.txt"):
                with open("baseball_posts.txt", "r") as f:
                    for line in f:
                        parts = line.strip().split("|", 1)
                        if len(parts) == 2:
                            post_id, content = parts
                            posts.append((post_id, content))
            
            # 날짜를 기준으로 내림차순 정렬
            posts.sort(key=lambda x: x[0], reverse=True)
            return posts

        def delete_post(post_id):
            posts = load_posts()
            posts = [post for post in posts if post[0] != post_id]
            with open("baseball_posts.txt", "w") as f:
                for pid, cont in posts:
                    f.write(f"{pid}|{cont}\n")

        st.title("야구 게시판")

        st.markdown(":red[자유롭게 게시할 수 있자만, 욕설과 비방은 삼가해 주세요. 자기의 닉네임을 게시글에 작성하면 본인 표시가 됩니다. 작성후 목록에서 수정과 삭제가 가능합니다.]")

        # 게시글 작성
        new_post = st.text_area("새 게시글 작성 ")
        if st.button("게시"):
            save_post(new_post)
            st.success("게시글이 저장되었습니다.")
            st.rerun()

        # 게시글 목록 표시 및 수정/삭제 기능
        st.subheader("게시글 목록")
        posts = load_posts()
        if not posts:
            st.info("게시된 글이 없습니다.")
        else:
            for post_id, content in posts:
                st.write(f"ID: {post_id}")
                st.write(content)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("수정", key=f"edit_button_{post_id}"):
                        st.session_state[f'edit_mode_{post_id}'] = True
                
                with col2:
                    if st.button("삭제", key=f"delete_{post_id}"):
                        delete_post(post_id)
                        st.success("게시글이 삭제되었습니다.")
                        st.rerun()

                if f'edit_mode_{post_id}' in st.session_state and st.session_state[f'edit_mode_{post_id}']:
                    edited_content = st.text_area("수정할 내용", content, key=f"edit_{post_id}")
                    if st.button("수정 완료", key=f"edit_complete_{post_id}"):
                        save_post(edited_content, post_id)
                        st.success("게시글이 수정되었습니다.")
                        del st.session_state[f'edit_mode_{post_id}']
                        st.rerun()
                    if st.button("취소", key=f"edit_cancel_{post_id}"):
                        del st.session_state[f'edit_mode_{post_id}']
                        st.rerun()

                st.markdown("---")

    elif game == "k":

        def save_post(content, post_id=None):
            if post_id is None:
                post_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            
            posts = load_posts()
            if post_id:
                posts = [post for post in posts if post[0] != post_id]
            posts.append((post_id, content))
            
            with open("basketball_posts.txt", "w") as f:
                for pid, cont in posts:
                    f.write(f"{pid}|{cont}\n")

        def load_posts():
            posts = []
            if os.path.exists("basketball_posts.txt"):
                with open("basketball_posts.txt", "r") as f:
                    for line in f:
                        parts = line.strip().split("|", 1)
                        if len(parts) == 2:
                            post_id, content = parts
                            posts.append((post_id, content))
            
            # 날짜를 기준으로 내림차순 정렬
            posts.sort(key=lambda x: x[0], reverse=True)
            return posts

        def delete_post(post_id):
            posts = load_posts()
            posts = [post for post in posts if post[0] != post_id]
            with open("basketball_posts.txt", "w") as f:
                for pid, cont in posts:
                    f.write(f"{pid}|{cont}\n")

        st.title("농구 게시판")

        st.markdown(":red[자유롭게 게시할 수 있자만, 욕설과 비방은 삼가해 주세요. 자기의 닉네임을 게시글에 작성하면 본인 표시가 됩니다. 작성후 목록에서 수정과 삭제가 가능합니다.]")

        # 게시글 작성
        new_post = st.text_area("새 게시글 작성 ")
        if st.button("게시"):
            save_post(new_post)
            st.success("게시글이 저장되었습니다.")
            st.rerun()

        # 게시글 목록 표시 및 수정/삭제 기능
        st.subheader("게시글 목록")
        posts = load_posts()
        if not posts:
            st.info("게시된 글이 없습니다.")
        else:
            for post_id, content in posts:
                st.write(f"ID: {post_id}")
                st.write(content)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("수정", key=f"edit_button_{post_id}"):
                        st.session_state[f'edit_mode_{post_id}'] = True
                
                with col2:
                    if st.button("삭제", key=f"delete_{post_id}"):
                        delete_post(post_id)
                        st.success("게시글이 삭제되었습니다.")
                        st.rerun()

                if f'edit_mode_{post_id}' in st.session_state and st.session_state[f'edit_mode_{post_id}']:
                    edited_content = st.text_area("수정할 내용", content, key=f"edit_{post_id}")
                    if st.button("수정 완료", key=f"edit_complete_{post_id}"):
                        save_post(edited_content, post_id)
                        st.success("게시글이 수정되었습니다.")
                        del st.session_state[f'edit_mode_{post_id}']
                        st.rerun()
                    if st.button("취소", key=f"edit_cancel_{post_id}"):
                        del st.session_state[f'edit_mode_{post_id}']
                        st.rerun()

                st.markdown("---")