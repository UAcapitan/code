<?php

namespace App\Controller;

use App\Entity\Dislikes;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Entity\Comments;
use App\Entity\Likes;

class DislikesController extends AbstractController
{
    /**
     * @Route("/dislike/{id}", name="dislike")
     */
    public function index(int $id): Response
    {

        $comment = $this->getDoctrine()->getRepository(Comments::class)->find($id);

        $likes = $this->getDoctrine()->getRepository(Likes::class)->findBy(['comment' => $id, 'user' => $comment->getUser()]);
        if ($likes) {
            $like = $likes[0];
        }

        $dislikes = $this->getDoctrine()->getRepository(Dislikes::class)->findBy(['comment' => $id, 'user' => $comment->getUser()]);

        $entityManager = $this->getDoctrine()->getManager();

        if (count($dislikes) == 0) {
            $dislike = new Dislikes();
            $dislike->setComment($comment);
            $dislike->setUser($this->getUser());
            $entityManager->persist($dislike);
            if ($likes) {
                $entityManager->remove($like);
            }
            $entityManager->flush();
        } else {
            $dislike = $dislikes[0];
            $entityManager->remove($dislike);
            $entityManager->flush();
        }

        return $this->redirectToRoute('campaign', ['id' => $comment->getCampaign()->getId()]);
    }
}
