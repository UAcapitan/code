<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Entity\Likes;
use App\Entity\Comments;
use App\Entity\Dislikes;

class LikesController extends AbstractController
{
    /**
     * @Route("/like/{id}", name="like")
     */
    public function index(int $id): Response
    {

        $comment = $this->getDoctrine()->getRepository(Comments::class)->find($id);

        $dislikes = $this->getDoctrine()->getRepository(Dislikes::class)->findBy(['comment' => $id, 'user' => $comment->getUser()]);
        if ($dislikes) {
            $dislike = $dislikes[0];
        }

        $likes = $this->getDoctrine()->getRepository(Likes::class)->findBy(['comment' => $id, 'user' => $comment->getUser()]);

        $entityManager = $this->getDoctrine()->getManager();

        if (count($likes) == 0) {
            $like = new Likes();
            $like->setComment($comment);
            $like->setUser($this->getUser());
            $entityManager->persist($like);
            $entityManager->flush();
            if ($dislikes) {
                $entityManager->remove($dislike);
            }
            $entityManager->flush();
        } else {
            $like = $likes[0];
            $entityManager->remove($like);
            $entityManager->flush();
        }

        return $this->redirectToRoute('campaign', ['id' => $comment->getCampaign()->getId()]);
    }
}
